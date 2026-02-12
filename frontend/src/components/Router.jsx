import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './screens/home/Home'
import Info from './screens/info/Info'

function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        
        {/* Вложенные маршруты для /cars */}
        <Route path="/cars">
          <Route path="brands/:id" element={<Home />} />
          <Route path=":id" element={<Info />} />
        </Route>
        <Route path="*" element={<div>Not found</div>} />
      </Routes>
    </BrowserRouter>
  );
}

export default Router