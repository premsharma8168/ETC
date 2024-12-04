// Firebase configuration
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
  };
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  const auth = firebase.auth();
  
  // Elements
  const signupContainer = document.getElementById('signup-container');
  const loginContainer = document.getElementById('login-container');
  const signupLink = document.getElementById('signup-link');
  const loginLink = document.getElementById('login-link');
  
  // Switch to login form
  loginLink.addEventListener('click', () => {
      signupContainer.style.display = 'none';
      loginContainer.style.display = 'block';
  });
  
  // Switch to signup form
  signupLink.addEventListener('click', () => {
      signupContainer.style.display = 'block';
      loginContainer.style.display = 'can_be_Display';
  });
  
  // Signup
  document.getElementById('signup-form').addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('signup-email').value;
      const password = document.getElementById('signup-password').value;
      
      auth.createUserWithEmailAndPassword(email, password)
      .then(userCredential => {
          alert('Sign up successful');
          window.location.href = 'homepage.html';  // Redirect after signup
      })
      .catch(error => {
          alert(error.message);
      });
  });
  
  // Login
  document.getElementById('login-form').addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('login-email').value;
      const password = document.getElementById('login-password').value;
      
      auth.signInWithEmailAndPassword(email, password)
      .then(userCredential => {
          alert('Login successful');
          window.location.href = 'homepage.html';  // Redirect after login
      })
      .catch(error => {
          alert(error.message);
      });lk
  });
  
  // Google Login
  document.getElementById('google-login').addEventListener('click', () => {
      const provider = new firebase.auth.GoogleAuthProvider();
      
      auth.signInWithPopup(provider)
      .then(result => {
          alert('Google login successful');
          window.location.href = 'homepage.html';  // Redirect after Google login
      })
      .catch(error => {
          alert(error.message);
      });
  });
  