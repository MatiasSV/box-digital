import React from 'react';
import './header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-logo">
        <img src="/logo-transparent-png.png" alt="PanelBox" />
      </div>
      <nav className="navbar">
        <ul className="nav-links">
          <li><a href="#inicio">Inicio</a></li>
          <li><a href="#nosotros">Nosotros</a></li>
          <li><a href="#servicios">Servicios</a></li>
          <li><a href="#contacto">Contacto</a></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
