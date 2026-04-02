import { useState } from "react";

export default function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    const res = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question })
    });

    const data = await res.json();
    setAnswer(data.answer);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>RAG Chat App</h1>

      <input
        type="text"
        placeholder="Ask your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={{ width: "400px", padding: "10px" }}
      />

      <button onClick={handleAsk} style={{ marginLeft: "10px", padding: "10px" }}>
        Ask
      </button>

      <div style={{ marginTop: "20px" }}>
        <h3>Answer:</h3>
        <p>{answer}</p>
      </div>
    </div>
  );
}