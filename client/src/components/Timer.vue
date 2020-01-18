<template>
<div class="timer">
  <div id="screen">00 : 00 : 00 : 00</div>
    <div class="buttons">
      <button class="emerald" onclick="start()">&#9658;</button>
      <button class="emerald" onclick="stop()">&#8718;</button>
      <button class="emerald" onclick="resume()">&#8634;</button>
      <button class="emerald" onclick="reset()">&#8635;</button>
   </div>
</div>
</template>

<style>
#screen {
  font-family: Calibri,Arial;
  font-weight: 80;
  font-size: 20px;
  color: black;
}

.buttons {
  padding-left: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.emerald {
  margin: 4px;
  color: #42b983;
  cursor: pointer;
  font-weight: 100px;
  font-size: 20px;
  outline: none;
  text-transform: uppercase;
  transition: all 0.2s ease;
}
</style>
