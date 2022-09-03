import React, { useState } from "react";
import axios from "axios";

const RegisterForm = (props) => {
  const { userData, setUserData } = props;
  // TODO fix bug stopping render
  // error handling
  const [errorMessage, setErrorMessage] = useState(null);

  // saving form inputs
  const [user, setUser] = useState({
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (e) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value,
    });
  };

  const register = (e) => {
    e.preventDefault();

    axios
      .post("http://localhost:4999/api/v1/user/register", user)
      .then((res) => {
        console.log(res.data);
        setUser({
          email: "",
          password: "",
          confirmPassword: "",
        });
        setUserData(res.data);
        setErrorMessage(null);
      })
      .catch((err) => {
        console.log(err);
        setErrorMessage(err.response.data.error);
      });
  };

  return (
    <div className="col card m-2 shadow">
      <h2 className="text-primary">Register</h2>
      <form onSubmit={register}>
        {errorMessage ? (
          <div className="alert alert-danger my-1">{errorMessage}</div>
        ) : null}
        <div className="form-group d-flex flex-column mb-3">
          <label htmlFor="email">Email:</label>
          <input
            className="form-control"
            type="email"
            name="email"
            value={user.email}
            onChange={(e) => {
              handleChange(e);
            }}
          />
        </div>
        <div className="form-group d-flex flex-column mb-3">
          <label htmlFor="password">Password:</label>
          <input
            className="form-control"
            type="password"
            name="password"
            value={user.password}
            onChange={(e) => {
              handleChange(e);
            }}
          />
        </div>
        <div className="form-group d-flex flex-column mb-3">
          <label htmlFor="confirmPassword">Confirm Password:</label>
          <input
            className="form-control"
            type="password"
            name="confirmPassword"
            value={user.confirmPassword}
            onChange={(e) => {
              handleChange(e);
            }}
          />
        </div>
        <input
          className="btn btn-outline-primary mb-3"
          type="submit"
          value="Register"
        />
      </form>
    </div>
  );
};

export default RegisterForm;
