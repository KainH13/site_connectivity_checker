import React from "react";

// components

const ConnectionCheckForm = (props) => {
  return (
    <div className="card p-2 m-2 shadow">
      <h2 className="text-center">What connections would you like to check?</h2>
      <form>
        <div className="row justify-content-center my-2">
          <button className="btn btn-primary" style={{width: "20rem"}}>Check Connections</button>
        </div>
        <div className="row align-items-center">
          <div className="col-6">
            <input className="form-control" type="text" placeholder="Enter URL" />
          </div>
          <div className="col-6">
            <div className="alert alert-success py-2 mb-0">Online</div>
            <div className="alert alert-danger py-2 mb-0">Offline</div>
          </div>
        </div>
        <div className="btn btn-secondary my-2">Add URL</div>
      </form>
    </div>
  );
};

export default ConnectionCheckForm;
