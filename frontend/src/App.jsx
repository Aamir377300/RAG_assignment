import { useState } from "react";

export default function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");
    try {
      const res = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      setAnswer(data.answer);
    } catch {
      setAnswer("Something went wrong. Make sure the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") handleAsk();
  };

  return (
    <div className="min-h-screen bg-[#0f0f13] flex items-center justify-center p-6">
      <div className="w-full max-w-2xl bg-[#1a1a24] border border-[#2e2e3e] rounded-2xl p-10 shadow-2xl">
        <h1 className="text-3xl font-bold text-gray-100 mb-2 tracking-tight text-center">RAG Chat</h1>
        <p className="text-gray-500 text-sm mb-8 text-center">Ask anything about the investment book</p>

        <div className="flex gap-3">
          <input
            type="text"
            placeholder="Ask your question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={handleKeyDown}
            className="flex-1 bg-[#0f0f13] border border-[#2e2e3e] text-gray-100 placeholder-gray-600 rounded-xl px-4 py-3 text-sm outline-none focus:border-violet-600 transition-colors"
          />
          <button
            onClick={handleAsk}
            disabled={loading}
            className="bg-violet-700 hover:bg-violet-600 disabled:opacity-50 disabled:cursor-not-allowed text-white font-semibold px-6 py-3 rounded-xl text-sm transition-colors"
          >
            {loading ? "..." : "Ask"}
          </button>
        </div>

        {(loading || answer) && (
          <div className="mt-6 bg-[#0f0f13] border border-[#2e2e3e] rounded-xl p-5">
            <p className="text-violet-500 text-xs font-semibold uppercase tracking-widest mb-3 text-center">Answer</p>
            <p className="text-gray-300 text-sm leading-relaxed whitespace-pre-wrap">
              {loading ? "Thinking..." : answer}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
