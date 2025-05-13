import { Route, Routes } from "react-router";
import Login from "../../pages/login/index.tsx";
import Register from "../../pages/register/index.tsx";
import Home from "../../pages/home/index.tsx";

export default function Routers() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/home" element={<Home />} />
    </Routes>
  );
}
