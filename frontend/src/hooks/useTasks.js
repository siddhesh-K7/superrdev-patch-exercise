import { useState, useEffect } from 'react';
import { fetchTasks } from '../api';

export function useTasks(query, status, page, pageSize) {
  const [tasks, setTasks] = useState([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    let ignore = false;
    const controller = new AbortController();

    const fetchCurrentTasks = async () => {
      setLoading(true);
      setError(null);
      
      try {
        const data = await fetchTasks({ query, status, page, pageSize, signal: controller.signal });
        if (!ignore) {
          setTasks(data.items);
          setTotal(data.total);
          setLoading(false);
        }
      } catch (err) {
        if (!ignore && err.name !== 'AbortError') {
          setError(err.message);
          setLoading(false);
        }
      }
    };

    const timerId = setTimeout(() => {
      fetchCurrentTasks();
    }, 300);

    return () => {
      ignore = true;
      clearTimeout(timerId);
      controller.abort();
    };
  }, [query, status, page, pageSize]);

  return { tasks, total, loading, error };
}
