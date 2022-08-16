import React from "react";

// components
import Navbar from "../components/Navbar";
import RegisterForm from "../components/RegisterForm";
import LoginForm from "../components/LoginForm";

const Login = (props) => {
  return (
    <div>
      <Navbar />
      <div className="row m-2">
        <RegisterForm />
        <LoginForm />
      </div>
    </div>
  );
};

export default Login;