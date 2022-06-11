import React from 'react';
import './Navbar.css';
import LogoGun from "../assets/icons-01.png";
import ShooterLogo from "../assets/sharpshotta.png";

function Navbar() {
    return(
    <div className='navbar'>
        <div className='farleft'>
            <img src={ShooterLogo} alt='red'/>
            <h1 style={{ color: 'white' }}>Shooter Stopper</h1>
        </div>
        <div className='leftSide'>
            <img src={LogoGun} alt='gun'/>
            <h1 style={{ color: 'white' }}>Gun Detection</h1>
            <img src={LogoGun} alt='gun'/>
            </div>
        <div className='rightSide'>
            <div className='navbar-titleText'>
                
            </div>
        </div>
    </div>
    );
}

export default Navbar;