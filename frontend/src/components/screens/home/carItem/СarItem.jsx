import React from 'react'
import styles from '../Home.module.css'
import { Link } from 'react-router-dom'

function СarItem({car}) {
  return (
    <div className={styles.carCard}>
        <img 
            src={car.image} 
            alt={`${car.brand} ${car.model}`} 
            className={styles.carImage}
        />
        <h2 className={styles.carName}>{car.name}</h2>
        <p className={styles.carPrice}>Цена: ${car.price}</p>
        <Link className='btn' to={`/cars/${car.id}`}>
        
            Подробнее</Link>
    </div>
  )
  
}

export default СarItem



