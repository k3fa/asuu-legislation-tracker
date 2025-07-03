import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'
import { supabase } from '../../lib/supabaseClient'
import '../../styles/globals.css'

interface Legislation {
  id: number
  title: string
  type: string
  status: string
  summary?: string
  document_url?: string
}

export default function LegislationPage() {
  const router = useRouter()
  const { id } = router.query
  const [item, setItem] = useState<Legislation | null>(null)

  useEffect(() => {
    if (!id) return
    supabase
      .from('legislation')
      .select('*')
      .eq('id', id)
      .single()
      .then(({ data }) => {
        if (data) setItem(data)
      })
  }, [id])

  if (!item) return <p className="p-4">Loading...</p>

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-2">{item.title}</h1>
      <p>Type: {item.type}</p>
      <p>Status: {item.status}</p>
      {item.summary && <p className="mt-4">{item.summary}</p>}
      {item.document_url && (
        <p className="mt-2">
          <a href={item.document_url} className="text-blue-600">Document</a>
        </p>
      )}
    </main>
  )
}
