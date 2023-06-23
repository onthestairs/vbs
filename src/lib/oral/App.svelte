<script>
  import oralSets from "../../data/oral/sets.json";
  let currentWord;
  let shouldPlay = true;
  let maxIterations = 5;
  let bufferSeconds = 1;

  const makeAudioFile = (word) => {
    return `/public/oral/audio/${word}.mp3`;
  };
  const play = async (set) => {
    let i = 0;
    let l = set.length;
    const audios = set.map((word) => {
      const url = makeAudioFile(word);
      let audioFile = new Audio(url);
      return audioFile;
    });
    console.log("Audios", audios);
    const playNext = () => {
      const iterations = i / l;
      if (iterations > maxIterations || !shouldPlay) {
        shouldPlay = true;
        return;
      }
      const index = i % l;
      console.log(`Playing ${index}`);
      const word = set[index];
      currentWord = word;
      const audioFile = audios[index];
      audioFile.play();
      i += 1;
    };
    audios.forEach(async (audio) => {
      audio.onended = () => {
        const delay = audio.duration + bufferSeconds;
        console.log(`Delaying for ${delay}`);
        setTimeout(() => playNext(), 1000 * delay);
      };
    });
    playNext();
  };
</script>

<main class="mx-auto max-w-5xl font-garamond">
  <div class="mb-12 mt-4 flex flex-col justify-between ">
    <h2 class="m-auto text-3xl font-bold underline">🇫🇷 Oral française 🇫🇷</h2>
  </div>
  {#each oralSets as set}
    <div>
      <input type="button" value="Play" on:click={() => play(set)} />
      {#each set as word}
        {#if word == currentWord}
          <p class="text-6xl font-bold text-red-600">{word}</p>
        {:else}
          <p class="text-6xl font-bold text-blue-600">{word}</p>
        {/if}
      {/each}
    </div>
  {/each}
</main>
