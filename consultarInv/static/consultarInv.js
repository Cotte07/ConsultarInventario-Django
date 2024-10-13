
const lista_producto = async()=>{
    try{
        const response = await fetch('http://127.0.0.1:8000/inventario/')
        const data = await response.json();

        let content = ``;
        data.producto.forEach((producto, PaginaPrincipal) => {
            content+=`
                <tr>
                    <td>${PaginaPrincipal} </td>
                    <td>${producto.nombre} </td>
                    <td>${producto.Proveedor} </td>
                </tr>
            `;
        });
        tablasInventario.innerHTML = content;
    }catch(ex){
        alert(ex);
    }
    
};

window.addEventListener('load', async()=>{
    await lista_producto();
});