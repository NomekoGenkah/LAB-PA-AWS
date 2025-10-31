import axios from 'axios';

function HomePage() {
  const handleDownload = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/v1/export/', {
        responseType: 'blob',
      });
      
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.download = 'reporte.csv';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Error downloading file:', error);
      alert('Error downloading file');
    }
  };

  return (
    <div>
      <h1>Welcome to the Home Page</h1>
      <p>This is the main landing page of our application.</p>
      <div className="button-holder">
        <button onClick={handleDownload}>Download Report</button>
        <button>Another Button</button>
        <button>Third Button</button>
        <button>Fourth Button</button>
      </div>

    </div>
  );
}

export default HomePage;