import React from "react";
import { Routes, Route } from "react-router-dom";

// bootstrap
import "bootstrap/dist/css/bootstrap.min.css";

// views
import Home from "./views/Home";
import Login from "./views/Login";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login / >} />
      </Routes>
    </div>
  );
}

export default App;
