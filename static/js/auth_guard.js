// Auth guard for protecting pages
import { auth } from './firebase_config.js';
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// Check if user is authenticated
onAuthStateChanged(auth, (user) => {
    if (!user) {
        // User is not logged in, redirect to login page
        window.location.href = '/auth/login';
    }
});