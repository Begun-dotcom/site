import React from 'react'
import styles from '../Home.module.css'
import { Link } from 'react-router-dom'



function СarBrand({carbrend}) {
    const handleClick = () => {
        console.log("Clicked car brand ID:", carbrend.id);
        console.log("Full object:", carbrend);
    };
    return (
    <Link 
        className={styles.carBrand} 
        to={`/cars/brands/${carbrend.id}`}
        onClick={handleClick}
    >
        <h2 className={styles.carName}>{carbrend.brand}</h2>
        
        
    </Link>
)
}

export default СarBrand