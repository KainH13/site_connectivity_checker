import React from "react";
import { Link } from "react-router-dom";

const Navbar = (props) => {
  const { userData, setUserData } = props;

  const logout = (e) => {
    setUserData(null);
  };

  return (
    <nav className="navbar navbar-light bg-light sticky-top">
      <div className="container-fluid justify-content-start">
        <Link className="navbar-brand text-secondary m-1" to="/">
          ConCheck
        </Link>
        <div className="nav m-1">
          {userData ? (
            <h2 className="text-secondary ms-3">
              Logged In As: {userData.user.email}
            </h2>
          ) : null}
          <Link className="btn btn-outline-primary ms-3" to="/login">
            Login
          </Link>
          <button className="btn btn-outline-danger ms-3" onClick={logout}>
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
