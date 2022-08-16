import React from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

const Navbar = (props) => {
  const navigate = useNavigate();

  const logout = (e) => {
    axios
      .post(
        "http://localhost:4999/api/v1/user/logout",
        {},
        {
          withCredentials: true,
        }
      )
      .then((res) => {
        console.log(res);
        localStorage.clear();
        navigate("/");
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <nav className="navbar navbar-light bg-light sticky-top">
      <div className="container-fluid justify-content-start">
        <h1 className="navbar-brand text-secondary m-1">ConCheck</h1>
        <div className="nav m-1">
          <Link className="nav-link" to="/">
            Check Connections
          </Link>
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
