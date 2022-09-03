import React from "react";

// components
import Navbar from "../components/Navbar";
import RegisterForm from "../components/RegisterForm";
import LoginForm from "../components/LoginForm";

// context
import userContext from "../context/userContext";

const Login = (props) => {
  return (
    <userContext.Consumer>
      {({ userData, setUserData }) => {
        return (
          <div>
            <Navbar userData={userData} setUserData={setUserData} />
            <div className="row m-2">
              <RegisterForm userData={userData} setUserData={setUserData} />
              <LoginForm userData={userData} setUserData={setUserData} />
            </div>
          </div>
        );
      }}
    </userContext.Consumer>
  );
};

export default Login;
