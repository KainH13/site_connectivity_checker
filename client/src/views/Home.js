import React from "react";

// components
import ConnectionCheckForm from "../components/ConnectionCheckForm";
import Navbar from "../components/Navbar";

const Home = (props) => {
  return (
    <div>
      <Navbar /> 
      <ConnectionCheckForm />
    </div>
  );
};

export default Home;
