from flask import Flask, render_template, request, jsonify, send_from_directory
import pyttsx3
import random
import os

app = Flask(__name__)

# Listas globais para armazenar os nomes
nomes = []
nomes_sorteados = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('static/audio', filename)

@app.route('/adicionar_nome', methods=['POST'])
def adicionar_nome():
    nome = request.json.get('nome', '').strip()
    if nome:
        nomes.append(nome)
        return jsonify({'success': True, 'nomes': nomes})
    return jsonify({'success': False, 'error': 'Nome vazio'})

@app.route('/realizar_sorteio', methods=['POST'])
def realizar_sorteio():
    nomes_disponiveis = [nome for nome in nomes if nome not in nomes_sorteados]
    
    if not nomes_disponiveis:
        return jsonify({
            'success': False, 
            'error': 'Todos os nomes já foram sorteados',
            'todosSort': True
        })
    
    nome_sorteado = random.choice(nomes_disponiveis)
    nomes_sorteados.append(nome_sorteado)
    
    return jsonify({
        'success': True,
        'vencedor': nome_sorteado,
        'restantes': len(nomes_disponiveis) - 1
    })

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    global nomes, nomes_sorteados
    nomes = []
    nomes_sorteados = []
    return jsonify({'success': True})

if __name__ == '__main__':
    # Garantir que a pasta de áudio existe
    os.makedirs('static/audio', exist_ok=True)
    app.run(debug=False, port=5000)