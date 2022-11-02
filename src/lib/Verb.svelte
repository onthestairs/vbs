<script>
  import Conjugation from "./Conjugation.svelte";

  export let verb;

  const startsWithAVowel = (word) => {
    return word.match("^[aeiou].*");
  };

  $: infinitive = verb.infinitive;
  $: wordReferenceLink = `https://www.wordreference.com/fren/${infinitive}#articleHead`;

  $: answers = verb.indicative.present;

  const reset = (verbInfinitive) => {
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
    reset(verb.infinitive);
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
</script>

<h2 class="mb-16 text-center text-8xl font-bold italic underline">
  {verb.infinitive}
</h2>

<div class="grid grid-cols-2 gap-4">
  <div>
    <iframe
      class="h-full w-128"
      src={wordReferenceLink}
      title="Word reference"
    />
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
