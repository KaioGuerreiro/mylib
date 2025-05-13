import { useRef } from "react";
import Api from "../../api/api";

export default function Register() {
  const emailRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);

  async function createUser() {
    try{
      await Api.post("/api/register/", { 
      username: emailRef.current?.value,
      password: passwordRef.current?.value,
      })
    } catch (error) {
      console.error("Erro ao criar conta:", error);
      alert("Erro ao criar sua conta.");
    }
    window.location.href = "/login";
    
  };

  return (
    <div className="flex flex-col items-center justify-center w-screen h-screen bg-neutral-950">
      <div className="flex flex-col items-center justify-center w-2/3 h-2/3 bg-neutral-200 rounded-lg shadow-lg">
        <img src="../../public/mylibLogo.png" alt="logo" className="w-100 p-10" />
        <h2 className="text-3xl font-bold mb-10 text-neutral-800">Cadastro</h2>
        <div className="flex flex-col w-3/4">
          <input
            ref={emailRef}
            type="email"
            required
            placeholder="Digite um email"
            className="mb-4 p-2 border border-gray-300 rounded bg-neutral-50"
          />
          <input
            ref={passwordRef}
            type="password"
            required
            placeholder="Digite uma senha"
            className="mb-4 p-2 border border-gray-300 rounded bg-neutral-50"
          />
          <button onClick={createUser} className="bg-neutral-900 text-neutral-50 p-2 rounded hover:bg-neutral-500 transition">
            Cadastrar
          </button>
        </div>

        <div className="flex flex-col items-center mt-4">
          <p className="text-neutral-800">Já tem uma conta?</p>
          <a href="/login" className="text-neutral-900 hover:underline transition">Faça login</a>
        </div>
      </div>
    </div>
  )
}
//   