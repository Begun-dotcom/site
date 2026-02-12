import React from 'react'
import {useState, useEffect} from 'react'
import {useParams } from "react-router-dom"
import CarItem from "../home/carItem/СarItem"
import styles from './Info.module.css'

function Info() {
    const [carInfo, getcarInfo] = useState([])
    const {id} = useParams()
    useEffect(() => {
        fetch(`http://localhost:8000/cars/${id}`)
        .then(res => res.json())
        .then(data => {
        getcarInfo(data)
      })
    
  
}, []);              
  return (
    <div className={styles.wrapper}>

        <header className= {styles.header}
        style={{backgroundImage: 'url(https://avatars.mds.yandex.net/get-autoru-vos/5234682/0f7ed2faff634307e4a8b6cf1921b59d/1200x900)'}}>
            <h1>ПРОДАЖА АВТОМОБИЛЕЙ</h1>
        </header>
        <aside></aside>  
        
        <main className={styles.main}>
            <CarItem car = {carInfo} />
        </main>

        <aside  className= {styles.asideright}>
                hello
        </aside>

    </div>

  )
}

export default Info
