import { Route, Routes } from 'react-router';
import Login from '../../pages/login';

export default function Routers() {
    return (
        <Routes>
            <Route path='/login' element={<Login />} />
        </Routes>
    )
}
