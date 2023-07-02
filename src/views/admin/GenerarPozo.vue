<template>
  <div class="container">
    <div class="formulario">
      <h1 class="titulo">Generar nuevo pozo</h1>
      <form @submit="guardarDatos">
        <div class="input-container">
          <label for="nombre">Nombre del pozo:</label>
          <input type="text" id="nombre" v-model="nombrePozo" required>
        </div>

        <div class="input-container">
          <label for="ubicacion">Ubicación del pozo:</label>
          <input type="text" id="ubicacion" v-model="ubicacionPozo" required>
        </div>

        <div class="input-container">
          <label for="concesion">Concesión (CONAGUA) del pozo:</label>
          <input type="text" id="concesion" v-model="concesionPozo" required>
        </div>

        <div class="input-container">
          <label for="convenio">Convenio (CFE) del pozo:</label>
          <input type="text" id="convenio" v-model="convenioPozo" required>
        </div>

        <div class="input-container grande">
          <label for="informacion">Información extra del pozo:</label>
          <textarea id="informacion" v-model="informacionExtraPozo"></textarea>
        </div>

        <button type="submit" class="boton-guardar">Guardar</button>
      </form>
    </div>
  </div>
</template>


<script>
export default {
  methods: {
    guardarDatos(event) {
      event.preventDefault();
      // Aquí puedes agregar la lógica para guardar los datos del formulario
      console.log('Datos guardados:', {
        nombre: this.nombrePozo,
        ubicacion: this.ubicacionPozo,
        concesion: this.concesionPozo,
        convenio: this.convenioPozo,
        informacionExtra: this.informacionExtraPozo
      });
      // Puedes llamar a una función o hacer una solicitud HTTP para guardar los datos
    }
  }
};
</script>

<style scoped>
.container {
  margin-top: 50px;
  background-image: url('/workspace/SIENAPA/image/fondo.jpg');
  background-size: cover;
  background-position: center;
  height: 100vh;
  position: relative;
}

.formulario {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.titulo {
  color: white;
  text-align: center;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  max-width: 600px;
}

.input-container {
  flex-basis: calc(50% - 10px);
  margin-bottom: 20px;
}

.input-container.grande {
  flex-basis: 100%;
}

label {
  color: white;
  margin-bottom: 10px;
  display: block;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 10px;
}

.boton-guardar {
  background-color: #1e2432;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

@media (max-width: 600px) {
  form {
    padding: 10px;
  }
  
  .input-container {
    flex-basis: 100%;
  }
}
</style>
