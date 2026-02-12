import React from 'react'
import {useState, useEffect} from 'react'
import {useParams } from "react-router-dom"
import styles from './Home.module.css'
import CarItem from './carItem/СarItem'
import СarBrend from './carItem/CarBrend'

export default function Home() {
    const {id} = useParams()
    const [cars, setCars] = useState([])
    const [carsBrend, setBrands] = useState([])
    
 
  useEffect(() => {
        const fetchCars = async () => {
            try {
                document.body.classList.add('updating');
                const url = id 
                    ? `http:///cars/brands/${id}`
                    : 'http:///cars';
//                     ? `http://localhost:8000/cars/brands/${id}`
//                     : 'http://localhost:8000/cars';

                
                console.log(`Fetching from: ${url}`);
                
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                console.log(`Loaded ${data.length} cars`);
                setCars(data);
                document.body.classList.remove('updating');
            } catch (error) {
                console.error("Error fetching cars:", error);
                // Можно показать сообщение об ошибке
            } 
        };
        
        fetchCars();
    }, [id]);
    
 useEffect(() => {
        const fetchBrands = async () => {
            try {
                const response = await fetch('http://localhost:8000/cars/brand');
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                console.log(`Loaded ${data.length} brands`);
                setBrands(data);
            } catch (error) {
                console.error("Error fetching brands:", error);
            } 
        };
        
        fetchBrands();
    }, []);

  return (
    <div className={styles.wrapper}>

        <header className= {styles.header}
        style={{backgroundImage: 'url(https://avatars.mds.yandex.net/get-autoru-vos/5234682/0f7ed2faff634307e4a8b6cf1921b59d/1200x900)'}}>
            <h1>ПРОДАЖА АВТОМОБИЛЕЙ</h1>
        </header>
        <aside  className= {styles.asideleft}>
                {carsBrend.map(carbrend => (
                    <СarBrend key={carbrend.id} carbrend = {carbrend}/>
                ))}
                
        </aside>
        
        <main className={styles.main}>
            {cars.map(car => (
                <CarItem key={car.id} car={car} />
                 
            ))}
        </main>

        <aside  className= {styles.asideright}>
                hello
        </aside>

    </div>
  )
}
