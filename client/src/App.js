import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";

// bootstrap
import "bootstrap/dist/css/bootstrap.min.css";

// views
import Home from "./views/Home";
import Login from "./views/Login";

// context
import userContext from "./context/userContext";

function App() {
  const [userData, setUserData] = useState(null);

  return (
    <div className="App">
      <userContext.Provider value={{ userData, setUserData }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </userContext.Provider>
    </div>
  );
}

export default App;
