// Adicionando um ouvinte de evento para o formulário de cadastro
document.getElementById('formLivro').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    // Pegando os valores dos campos de entrada
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    const ano = document.getElementById('ano').value;
    const genero = document.getElementById('genero').value;
    const capa = document.getElementById('capa').files[0]; // Pegando a imagem da capa

    // Validando se todos os campos estão preenchidos
    if (!titulo || !autor || !ano || !genero || !capa) {
        alert('Todos os campos são obrigatórios!'); // Alerta de erro
        return;
    }

    // Criando um objeto livro com os dados inseridos
    const livro = {
        id: Date.now(), // Gerando um ID único com a data e hora atual
        titulo,
        autor,
        ano,
        genero,
        capa: URL.createObjectURL(capa) // Criando uma URL temporária para a capa do livro
    };

    // Recuperando os livros já cadastrados no LocalStorage
    let livros = JSON.parse(localStorage.getItem('livros')) || [];
    livros.push(livro); // Adicionando o novo livro à lista
    localStorage.setItem('livros', JSON.stringify(livros)); // Salvando novamente no LocalStorage

    // Limpando o formulário
    document.getElementById('formLivro').reset();

    // Atualizando a lista de livros
    renderizarLivros();
});

// Função para renderizar os livros cadastrados na tabela
function renderizarLivros() {
    const livros = JSON.parse(localStorage.getItem('livros')) || []; // Recuperando livros do LocalStorage
    const tbody = document.getElementById('livrosTbody');
    tbody.innerHTML = ''; // Limpando a tabela antes de adicionar novos itens

    // Percorrendo cada livro e criando uma linha na tabela
    livros.forEach(livro => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><img src="${livro.capa}" alt="Capa do livro" style="width: 50px; height: 75px;"></td>
            <td>${livro.titulo}</td>
            <td>${livro.autor}</td>
            <td>${livro.ano}</td>
            <td>${livro.genero}</td>
            <td>
                <button class="edit" onclick="editarLivro(${livro.id})">Editar</button>
                <button class="delete" onclick="deletarLivro(${livro.id})">Deletar</button>
            </td>
        `;
        tbody.appendChild(tr); // Adicionando a linha na tabela
    });
}

// Função para editar um livro (lógica ainda não implementada)
function editarLivro(id) {
    // A lógica de edição será implementada aqui
    alert('Funcionalidade de edição ainda não implementada.');
}

// Função para deletar um livro da lista
function deletarLivro(id) {
    let livros = JSON.parse(localStorage.getItem('livros')) || []; // Recuperando os livros do LocalStorage
    livros = livros.filter(livro => livro.id !== id); // Removendo o livro com o ID correspondente
    localStorage.setItem('livros', JSON.stringify(livros)); // Salvando novamente no LocalStorage

    // Atualizando a lista de livros
    renderizarLivros();
}

// Chamada inicial para renderizar os livros cadastrados ao carregar a página
renderizarLivros();
