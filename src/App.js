import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="hero">
        <h1>Welcome to My Portfolio</h1>
        <p>Full Stack Developer & UI/UX Enthusiast</p>
      </header>

      <section className="projects">
        <h2>Featured Projects</h2>
        <div className="project-grid">
          <div className="project-card">
            <h3>Project 1</h3>
            <p>A React-based web application</p>
            <button className="btn">Learn More</button>
          </div>
          <div className="project-card">
            <h3>Project 2</h3>
            <p>Mobile-first responsive design</p>
            <button className="btn">Learn More</button>
          </div>
          <div className="project-card">
            <h3>Project 3</h3>
            <p>Full-stack application with Node.js</p>
            <button className="btn">Learn More</button>
          </div>
        </div>
      </section>

      <section className="contact">
        <h2>Get In Touch</h2>
        <div className="contact-form">
          <input type="email" placeholder="Your Email" />
          <textarea placeholder="Your Message"></textarea>
          <button className="btn btn-primary">Send Message</button>
        </div>
      </section>
    </div>
  );
}

export default App;