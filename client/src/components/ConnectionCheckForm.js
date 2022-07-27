import React, { useState } from "react";
import axios from "axios";

// components

const ConnectionCheckForm = (props) => {
  const [urls, setUrls] = useState([""]);
  const [results, setResults] = useState(false);
  const [resultData, setResultData] = useState({});

  const addUrl = () => {
    let newUrls = [...urls];
    newUrls.push("");
    setUrls(newUrls);
  };

  const changeHandler = (e, index) => {
    let tempUrls = [...urls];
    tempUrls[index] = e.target.value;
    setUrls(tempUrls);
  };

  const checkConnections = (e) => {
    e.preventDefault();

    axios
      .post("http://localhost:4999/api/v1/connectivity_check/basic", {
        urls: urls,
      })
      .then((res) => {
        console.log("response: ", res);
        console.log("response data: ", res.data);
        setResultData(res.data);
        setResults(true);
      })
      .catch((err) => {
        console.log(err);
        console.log(err.response.data);
      });
  };

  return (
    <div className="card p-2 m-2 shadow">
      <h2 className="text-center">What connections would you like to check?</h2>
      <form onSubmit={checkConnections}>
        <div className="row justify-content-center my-2">
          <button className="btn btn-primary" style={{ width: "20rem" }}>
            Check Connections
          </button>
        </div>
        {urls.map((url, index) => {
          return (
            <div className="row align-items-center my-2" key={index}>
              <div className="col-6">
                <input
                  className="form-control"
                  type="text"
                  placeholder="Enter URL"
                  value={url}
                  onChange={(e) => changeHandler(e, index)}
                />
              </div>
              <div className="col-6">
                {results && resultData[url] !== undefined ? (
                  <div>
                    {resultData[url]["status"] === "Online" ? (
                      <div className="alert alert-success py-2 mb-0">
                        Online
                      </div>
                    ) : (
                      <div className="alert alert-danger py-2 mb-0">
                        Offline: {resultData[url]["error"]}
                      </div>
                    )}
                  </div>
                ) : null}
              </div>
            </div>
          );
        })}
        <div className="btn btn-secondary my-2" onClick={addUrl}>
          Add URL
        </div>
      </form>
    </div>
  );
};

export default ConnectionCheckForm;
