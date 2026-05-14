const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 21114;
const SECRET_KEY = 'teamdesk-secret-key';

app.use(cors());
app.use(bodyParser.json());

const DB_FILE = path.join(__dirname, 'db.json');

// Initialize database if not exists
if (!fs.existsSync(DB_FILE)) {
    const initialDb = {
        users: [
            {
                username: 'admin',
                password: 'password123',
                display_name: 'TeamDesk Admin',
                email: 'admin@teamdesk.com',
                address_book: [
                    { id: '123456789', name: 'Support PC', platform: 'Windows' }
                ]
            }
        ]
    };
    fs.writeFileSync(DB_FILE, JSON.stringify(initialDb, null, 2));
}

function getDb() {
    return JSON.parse(fs.readFileSync(DB_FILE, 'utf8'));
}

function saveDb(db) {
    fs.writeFileSync(DB_FILE, JSON.stringify(db, null, 2));
}

// Required for TeamDesk client to detect server status
app.get('/api/login-options', (req, res) => {
    res.json({
        oidc: false,
        email: true
    });
});

app.post('/api/login', (req, res) => {
    const { username, password, id, uuid } = req.body;
    const db = getDb();
    const user = db.users.find(u => u.username === username && u.password === password);

    if (user) {
        const token = jwt.sign({ username: user.username }, SECRET_KEY, { expiresIn: '7d' });
        res.json({
            access_token: token,
            type: 'access_token',
            user: {
                name: user.username,
                display_name: user.display_name,
                email: user.email,
                status: 1,
                info: {}
            }
        });
    } else {
        res.status(401).json({ error: 'Invalid credentials' });
    }
});

app.get('/api/ab', (req, res) => {
    const token = req.headers.authorization?.split(' ')[1];
    if (!token) return res.status(401).json({ error: 'No token provided' });

    try {
        const decoded = jwt.verify(token, SECRET_KEY);
        const db = getDb();
        const user = db.users.find(u => u.username === decoded.username);
        res.json({
            data: JSON.stringify(user.address_book || [])
        });
    } catch (err) {
        res.status(401).json({ error: 'Invalid token' });
    }
});

app.post('/api/ab', (req, res) => {
    const token = req.headers.authorization?.split(' ')[1];
    if (!token) return res.status(401).json({ error: 'No token provided' });

    try {
        const decoded = jwt.verify(token, SECRET_KEY);
        const db = getDb();
        const userIndex = db.users.findIndex(u => u.username === decoded.username);
        
        const newEntry = req.body;
        db.users[userIndex].address_book = db.users[userIndex].address_book || [];
        db.users[userIndex].address_book.push(newEntry);
        
        saveDb(db);
        res.json({ success: true });
    } catch (err) {
        res.status(401).json({ error: 'Invalid token' });
    }
});

app.get('/api/user', (req, res) => {
    const token = req.headers.authorization?.split(' ')[1];
    if (!token) return res.status(401).json({ error: 'No token provided' });

    try {
        const decoded = jwt.verify(token, SECRET_KEY);
        const db = getDb();
        const user = db.users.find(u => u.username === decoded.username);
        res.json(user);
    } catch (err) {
        res.status(401).json({ error: 'Invalid token' });
    }
});

app.listen(PORT, () => {
    console.log(`TeamDesk Account Server running on port ${PORT}`);
});
