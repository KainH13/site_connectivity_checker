import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const LoginForm = (props) => {
  const { userData, setUserData } = props;

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const login = (e) => {
    e.preventDefault();
    axios
      .post(
        "http://localhost:4999/api/v1/user/login",
        {
          email: email,
          password: password,
        },
      )
      .then((res) => {
        console.log("response: ", res);
        console.log("response data: ", res.data);
        setUserData(res.data)
        navigate("/");
      })
      .catch((err) => {
        console.log(err);
        setErrorMessage(err.response.data.error);
      });
  };

  return (
    <div className="col card m-2 shadow">
      <h2 className="text-success">Login</h2>
      <form onSubmit={login}>
        {errorMessage ? (
          <div className="alert alert-danger my-1">{errorMessage}</div>
        ) : null}
        <div className="form-group d-flex flex-column mb-3">
          <label htmlFor="email">Email:</label>
          <input
            className="form-control"
            type="email"
            name="email"
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="form-group d-flex flex-column mb-3">
          <label htmlFor="password">Password:</label>
          <input
            className="form-control"
            type="password"
            name="password"
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <input
          className="btn btn-outline-success mb-2"
          type="submit"
          value="Login"
        />
      </form>
    </div>
  );
};

export default LoginForm;
