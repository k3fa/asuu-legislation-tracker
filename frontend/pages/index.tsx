import { useEffect, useState } from 'react'
import Link from 'next/link'
import { supabase } from '../lib/supabaseClient'
import '../styles/globals.css'

interface Legislation {
  id: number
  title: string
  type: string
  status: string
  introduced_date?: string
}

export default function Home() {
  const [items, setItems] = useState<Legislation[]>([])

  useEffect(() => {
    supabase
      .from('legislation')
      .select('*')
      .then(({ data }) => {
        if (data) setItems(data)
      })
  }, [])

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">ASUU Legislation</h1>
      <Link href="/new" className="text-blue-600">Add New</Link>
      <table className="min-w-full mt-4">
        <thead>
          <tr>
            <th className="text-left">Title</th>
            <th className="text-left">Type</th>
            <th className="text-left">Status</th>
          </tr>
        </thead>
        <tbody>
          {items.map(item => (
            <tr key={item.id} className="border-t">
              <td>
                <Link href={`/legislation/${item.id}`}>{item.title}</Link>
              </td>
              <td>{item.type}</td>
              <td>{item.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  )
}
