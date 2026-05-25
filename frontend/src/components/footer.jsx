import React from 'react';
import './footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>&copy; 2024 PanelBox. Todos los derechos reservados.</p>
        <ul className="footer-links">
          <li><a href="#terminos">Términos y Condiciones</a></li>
          <li><a href="#privacidad">Política de Privacidad</a></li>
        </ul>
      </div>
    </footer>
  );
};

export default Footer;
