import { useRef, useEffect } from "react";
import Api from "../../api/api";

export default function Login() {
  const token = localStorage.getItem("token");
  useEffect(() => {
    if (token) {
      window.location.href = "/home";
    }
  }, [token]);

  const emailRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);

  async function loginUser() {
    try{
      const response = await Api.post("/api/login", { 
      username: emailRef.current?.value,
      password: passwordRef.current?.value,
      })
      const token = response.data.token;
      console.log(token);
      localStorage.setItem("token", token);
    } catch (error) {
      console.error("Erro ao fazer login:", error);
      alert("Erro ao fazer login. Verifique suas credenciais.");
    }
    
  };

  return (
    <div className="flex flex-col items-center justify-center w-screen h-screen bg-neutral-950">
      <div className="flex flex-col items-center justify-center w-2/3 h-2/3 bg-neutral-200 rounded-lg shadow-lg">
        <img src="../../public/mylibLogo.png" alt="logo" className="w-100 p-10" />
        <h2 className="text-3xl font-bold mb-10 text-neutral-800">Login</h2>
        <div className="flex flex-col w-3/4">
          <input
            ref={emailRef}
            type="email"
            required
            placeholder="Digite seu email"
            className="mb-4 p-2 border border-gray-300 rounded bg-neutral-50"
          />
          <input
            ref={passwordRef}
            type="password"
            required
            placeholder="Digite sua senha"
            className="mb-4 p-2 border border-gray-300 rounded bg-neutral-50"
          />
          <button onClick={loginUser} className="bg-neutral-900 text-neutral-50 p-2 rounded hover:bg-neutral-500 transition">
            Login
          </button>
        </div>

        <p className="mt-4 text-gray-400">
          Ainda não tem uma conta?{" "}
          <a href="/register" className="text-neutral-900 hover:underline">
            Registre-se
          </a>
        </p>
        <p className="mt-4 text-gray-400">
          <a href="/forgot-password" className="text-neutral-900 hover:underline">
            Esqueceu a senha?
          </a>
        </p>
      </div>
    </div>
  );
}
