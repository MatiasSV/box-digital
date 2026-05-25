import React from 'react';
import './logincard.css';

const LoginCard = () => {
  return (
    <div className="login-card">
      <h3 className="login-title">¡Bienvenido!</h3>
      <form className="login-form">
        <div className="form-group">
          <label htmlFor="rut">Rut</label>
          <input type="text" id="rut" name="rut" placeholder="12.345.678-9" />
        </div>
        <div className="form-group">
          <label htmlFor="password">Contraseña</label>
          <input type="password" id="password" name="password" placeholder="********" />
        </div>
        <button type="submit" className="login-btn">Iniciar Sesión</button>
      </form>
    </div>
  );
};

export default LoginCard;
