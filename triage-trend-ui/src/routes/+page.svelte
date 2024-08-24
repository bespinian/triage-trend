<script lang="ts">
	import type { Prediction } from '../lib/Prediction';


	const startDate: string = (new Date()).toISOString().split('T')[0];
	const predictionMap: Map<string, Prediction> = new Map<string, Prediction>();

	interface RequestPayload {
    date: string;
  }
	

  // Function to send the POST request
  async function postData(date: string): Promise<void> {
    const payload: RequestPayload = {
      date: date,
    };

    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data: Prediction = await response.json();
      predictionMap.set(date, data);  // Update the state with the response data
    } catch (err) {
    	err instanceof Error ? err.message : 'Unknown error';
    }
  }

	let isLoaded = false;
	async function loadData() {
	  let i = 0;
		for (; i < 8; i++) {
			await postData(offsetDate(startDate, i));
		}
		isLoaded = true;
	}
    
	function roundedPrediction(date: string): number {
		let prediction = predictionMap.get(date);
		if (prediction) {
			return Math.ceil(prediction.prediction);
		} else {
			return 0;
		}
	}

	function predictionColor(prediction: number): string {
		if (prediction >= 15) {
			return 'bg-error';
		} else if (prediction < 15 && prediction >= 7) {
			return 'bg-warning';
		} else {
			return 'bg-neutral-content';
		}
	}

	function dateText(date: string): string {
		let dateObj = new Date(date);
		const swissGermanDateText = dateObj.toLocaleDateString('de-CH', {
			weekday: 'long',
			day: 'numeric',
			month: 'long',
			year: 'numeric'
		});
		return swissGermanDateText;
	}

	function offsetDate(date: string, offset: number): string {
		const dateObj = new Date(date);

		dateObj.setDate(dateObj.getDate() + offset);

		return dateObj.toISOString().split('T')[0];
	}

	loadData();
</script>
{#if isLoaded}
<div class="h-full mx-auto">
	<div class="hero min-h-[50vh]">
		<div class="flex">
			<div class="mr-80">
				<img src="./clienia-logo.svg" class="" alt="The logo" />
			</div>
			<div class="card shadow-xl {predictionColor(roundedPrediction(startDate))}">
				<div class="card-body">
					<h1 class="card-title text-center">{dateText(startDate)}</h1>
					<p class="text-9xl text-center">
						{roundedPrediction(startDate)}
					</p>
				</div>
			</div>
		</div>
	</div>
	<div class="container mx-auto grid grid-cols-7 gap-2">
		{#each { length: 7 } as _, i}
			<div class="card {predictionColor(roundedPrediction(offsetDate(startDate, i + 1)))}">
				<div class="card-body">
					<span class="text-center text-xl font-bold"
						>{dateText(offsetDate(startDate, i + 1)).split(',')[0]}</span
					>
					<span class="text-center text-m"
						>{dateText(offsetDate(startDate, i + 1)).split(',')[1]}</span
					>
					<p class="text-6xl align-middle text-center">
						{roundedPrediction(offsetDate(startDate, i + 1))}
					</p>
				</div>
			</div>
		{/each}
	</div>
</div>
{/if}
