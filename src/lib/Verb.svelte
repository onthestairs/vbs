<script>
  import Conjugation from "./Conjugation.svelte";

  export let verb;
  export let verbForm;
  export let allCorrect;

  $: [mood, tense] = verbForm.split("-");

  const startsWithAVowel = (word) => {
    return word.match("^[aeioué].*");
  };

  $: infinitive = verb.infinitive;

  $: answers = verb[mood][tense];

  const reset = (verbInfinitive, mood, tense) => {
    console.log("infinitive is", verbInfinitive);
    firstPersonSingular = "";
    secondPersonSingular = "";
    thirdPersonSingular = "";
    firstPersonPlural = "";
    secondPersonPlural = "";
    thirdPersonPlural = "";
    // finally, focus the first element
    if (!!firstPersonSingularInput) {
      firstPersonSingularInput.focus();
    }
  };
  $: {
    // reset the answers if the infinitive has changed
    reset(infinitive, mood, tense);
  }

  let firstPersonSingularInput;
  let firstPersonSingular = "";
  $: firstPersonSingularCorrect =
    firstPersonSingular === answers.first_person_singular;
  $: if (firstPersonSingularCorrect) {
    secondPersonSingularInput.focus();
  }
  $: firstPersonSingularPronoun = startsWithAVowel(
    answers.first_person_singular
  )
    ? "J'"
    : "Je";

  let secondPersonSingularInput;
  let secondPersonSingular = "";
  $: secondPersonSingularCorrect =
    secondPersonSingular === answers.second_person_singular;
  $: if (secondPersonSingularCorrect) {
    thirdPersonSingularInput.focus();
  }

  let thirdPersonSingularInput;
  let thirdPersonSingular = "";
  $: thirdPersonSingularCorrect =
    thirdPersonSingular === answers.third_person_singular;
  $: if (thirdPersonSingularCorrect) {
    firstPersonPluralInput.focus();
  }

  let firstPersonPluralInput;
  let firstPersonPlural = "";
  $: firstPersonPluralCorrect =
    firstPersonPlural === answers.first_person_plural;
  $: if (firstPersonPluralCorrect) {
    secondPersonPluralInput.focus();
  }

  let secondPersonPluralInput;
  let secondPersonPlural = "";
  $: secondPersonPluralCorrect =
    secondPersonPlural === answers.second_person_plural;
  $: if (secondPersonPluralCorrect) {
    thirdPersonPluralInput.focus();
  }

  let thirdPersonPluralInput;
  let thirdPersonPlural = "";
  $: thirdPersonPluralCorrect =
    thirdPersonPlural === answers.third_person_plural;

  $: allCorrect =
    firstPersonSingularCorrect &&
    secondPersonSingularCorrect &&
    thirdPersonSingularCorrect &&
    firstPersonPluralCorrect &&
    secondPersonPluralCorrect &&
    thirdPersonPluralCorrect;

  $: frenchMood = {
    indicative: "indicatif",
    subjunctive: "subjontif",
  }[mood];
  $: frenchTense = {
    present: "présent",
    future: "futur",
    imperfect: "imperfait",
  }[tense];
</script>

<div class="grid grid-cols-2 gap-4">
  <div>
    <h4 class="mb-6 text-center text-4xl font-bold ">
      Mode: <span class="text-purple-800">{frenchMood}</span><br />
      Tense: <span class="text-orange-600">{frenchTense} </span>
    </h4>
    <h2 class="mb-16 text-center text-8xl font-bold italic underline">
      {verb.infinitive}
    </h2>
    {#each verb.english as englishVerb, index}
      <h3 class="text-center text-4xl italic ">
        {index + 1}. to {englishVerb}
      </h3>
    {/each}
  </div>
  <div class="flex flex-col text-3xl">
    <Conjugation
      pronoun={firstPersonSingularPronoun}
      bind:value={firstPersonSingular}
      bind:inputRef={firstPersonSingularInput}
      isCorrect={firstPersonSingularCorrect}
      revealAnswer={() => {
        firstPersonSingular = answers.first_person_singular;
      }}
    />
    <Conjugation
      pronoun="Tu"
      bind:value={secondPersonSingular}
      isCorrect={secondPersonSingularCorrect}
      bind:inputRef={secondPersonSingularInput}
      revealAnswer={() => {
        secondPersonSingular = answers.second_person_singular;
      }}
    />
    <Conjugation
      pronoun="Il/Elle/On"
      bind:value={thirdPersonSingular}
      isCorrect={thirdPersonSingularCorrect}
      bind:inputRef={thirdPersonSingularInput}
      revealAnswer={() => {
        thirdPersonSingular = answers.third_person_singular;
      }}
    />
    <Conjugation
      pronoun="Nous"
      bind:value={firstPersonPlural}
      isCorrect={firstPersonPluralCorrect}
      bind:inputRef={firstPersonPluralInput}
      revealAnswer={() => {
        firstPersonPlural = answers.first_person_plural;
      }}
    />
    <Conjugation
      pronoun="Vous"
      bind:value={secondPersonPlural}
      isCorrect={secondPersonPluralCorrect}
      bind:inputRef={secondPersonPluralInput}
      revealAnswer={() => {
        secondPersonPlural = answers.second_person_plural;
      }}
    />
    <Conjugation
      pronoun="Ils/Elles"
      bind:value={thirdPersonPlural}
      isCorrect={thirdPersonPluralCorrect}
      bind:inputRef={thirdPersonPluralInput}
      revealAnswer={() => {
        thirdPersonPlural = answers.third_person_plural;
      }}
    />
  </div>
</div>
