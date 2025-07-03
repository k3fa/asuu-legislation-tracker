import { useState } from 'react'
import { useRouter } from 'next/router'
import { supabase } from '../lib/supabaseClient'
import '../styles/globals.css'

export default function NewLegislation() {
  const router = useRouter()
  const [title, setTitle] = useState('')
  const [type, setType] = useState('Senate')
  const [status, setStatus] = useState('Draft')

  async function submit() {
    const { error } = await supabase.from('legislation').insert({ title, type, status })
    if (!error) router.push('/')
  }

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">New Legislation</h1>
      <div className="mb-2">
        <label className="block">Title</label>
        <input className="border p-1" value={title} onChange={e => setTitle(e.target.value)} />
      </div>
      <div className="mb-2">
        <label className="block">Type</label>
        <select className="border p-1" value={type} onChange={e => setType(e.target.value)}>
          <option>Senate</option>
          <option>Assembly</option>
          <option>Joint</option>
        </select>
      </div>
      <div className="mb-2">
        <label className="block">Status</label>
        <input className="border p-1" value={status} onChange={e => setStatus(e.target.value)} />
      </div>
      <button className="bg-blue-600 text-white px-2 py-1" onClick={submit}>Save</button>
    </main>
  )
}
