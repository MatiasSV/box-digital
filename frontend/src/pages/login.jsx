import React from 'react';
import LoginCard from '../components/logincard';
import './login.css';

const Login = () => {
  return (
    <div className="login-page">
      <div className="login-info">
        <img src="/logo panelbox con eslogan.png" alt="PanelBox Logo" className="login-logo-main" />
        <h2>La solución fácil para reservar horas en un mismo lugar.</h2>
        <ul className="login-features">
          <li>✔️ Gestiona tus reservas</li>
          <li>✔️ Monitorea tus horarios</li>
          <li>✔️ Optimiza la atención</li>
        </ul>
      </div>
      <div className="login-card-container">
        <LoginCard />
      </div>
    </div>
  );
};

export default Login;
