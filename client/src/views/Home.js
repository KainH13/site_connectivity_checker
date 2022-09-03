import React from "react";

// components
import ConnectionCheckForm from "../components/ConnectionCheckForm";
import Navbar from "../components/Navbar";

// context
import userContext from "../context/userContext";

const Home = (props) => {
  return (
    <userContext.Consumer>
      {({ userData, setUserData }) => {
        return (
          <div>
            <Navbar userData={userData} setUserData={setUserData} />
            <ConnectionCheckForm userData={userData} setUserData={setUserData} />
          </div>
        );
      }}
    </userContext.Consumer>
  );
};

export default Home;
