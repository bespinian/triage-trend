<script lang="ts">
	import type { Prediction } from '../lib/Prediction';

	const startDate: string = '2024-08-25';
	const predictionMap: Map<string, Prediction> = new Map<string, Prediction>();

	predictionMap.set('2024-08-25', {
		prediction: 2.5,
		featuresUsed: {
			averageTemperature: 20.0,
			maxTemperature: 25.0,
			totalRainDuration: 2.0,
			averagePressure: 1010.0,
			averageGlobalRadiation: 220.0,
			cloudiness: 0.3,
			moonPhase: 40.0,
			isVacationAargau: 0,
			isVacationZug: 0,
			isVacationSchwyz: 0,
			isVacationStGallen: 0,
			isVacationSchaffhausen: 0,
			isVacationThurgau: 0,
			weekday: 5,
			isWeekend: 1,
			aargauWeekAfterHoliday: 0,
			aargauFirstWeekOfHoliday: 0,
			zugWeekAfterHoliday: 0,
			zugFirstWeekOfHoliday: 0,
			schwyzWeekAfterHoliday: 0,
			schwyzFirstWeekOfHoliday: 0,
			stGallenWeekAfterHoliday: 0,
			stGallenFirstWeekOfHoliday: 0,
			schaffhausenWeekAfterHoliday: 0,
			schaffhausenFirstWeekOfHoliday: 0,
			thurgauWeekAfterHoliday: 0,
			thurgauFirstWeekOfHoliday: 0,
			averageTemperature5dayMean: 19.5,
			maxTemperature5dayMean: 24.5,
			totalRainDuration5dayMean: 1.8,
			averagePressure5dayMean: 1012.0,
			averageGlobalRadiation5dayMean: 215.0,
			cloudiness5dayMean: 0.25,
			publicHolidayAargau: 0,
			publicHolidayZug: 0,
			publicHolidaySchwyz: 0,
			publicHolidayStGallen: 0,
			publicHolidayThurgau: 0,
			publicHolidaySchaffhausen: 0,
			publicHolidayZurich: 0
		}
	});
	predictionMap.set('2024-08-26', {
		prediction: 7,
		featuresUsed: {
			averageTemperature: 20.0,
			maxTemperature: 25.0,
			totalRainDuration: 2.0,
			averagePressure: 1010.0,
			averageGlobalRadiation: 220.0,
			cloudiness: 0.3,
			moonPhase: 40.0,
			isVacationAargau: 0,
			isVacationZug: 0,
			isVacationSchwyz: 0,
			isVacationStGallen: 0,
			isVacationSchaffhausen: 0,
			isVacationThurgau: 0,
			weekday: 5,
			isWeekend: 1,
			aargauWeekAfterHoliday: 0,
			aargauFirstWeekOfHoliday: 0,
			zugWeekAfterHoliday: 0,
			zugFirstWeekOfHoliday: 0,
			schwyzWeekAfterHoliday: 0,
			schwyzFirstWeekOfHoliday: 0,
			stGallenWeekAfterHoliday: 0,
			stGallenFirstWeekOfHoliday: 0,
			schaffhausenWeekAfterHoliday: 0,
			schaffhausenFirstWeekOfHoliday: 0,
			thurgauWeekAfterHoliday: 0,
			thurgauFirstWeekOfHoliday: 0,
			averageTemperature5dayMean: 19.5,
			maxTemperature5dayMean: 24.5,
			totalRainDuration5dayMean: 1.8,
			averagePressure5dayMean: 1012.0,
			averageGlobalRadiation5dayMean: 215.0,
			cloudiness5dayMean: 0.25,
			publicHolidayAargau: 0,
			publicHolidayZug: 0,
			publicHolidaySchwyz: 0,
			publicHolidayStGallen: 0,
			publicHolidayThurgau: 0,
			publicHolidaySchaffhausen: 0,
			publicHolidayZurich: 0
		}
	});
	predictionMap.set('2024-08-27', {
		prediction: 9,
		featuresUsed: {
			averageTemperature: 20.0,
			maxTemperature: 25.0,
			totalRainDuration: 2.0,
			averagePressure: 1010.0,
			averageGlobalRadiation: 220.0,
			cloudiness: 0.3,
			moonPhase: 40.0,
			isVacationAargau: 0,
			isVacationZug: 0,
			isVacationSchwyz: 0,
			isVacationStGallen: 0,
			isVacationSchaffhausen: 0,
			isVacationThurgau: 0,
			weekday: 5,
			isWeekend: 1,
			aargauWeekAfterHoliday: 0,
			aargauFirstWeekOfHoliday: 0,
			zugWeekAfterHoliday: 0,
			zugFirstWeekOfHoliday: 0,
			schwyzWeekAfterHoliday: 0,
			schwyzFirstWeekOfHoliday: 0,
			stGallenWeekAfterHoliday: 0,
			stGallenFirstWeekOfHoliday: 0,
			schaffhausenWeekAfterHoliday: 0,
			schaffhausenFirstWeekOfHoliday: 0,
			thurgauWeekAfterHoliday: 0,
			thurgauFirstWeekOfHoliday: 0,
			averageTemperature5dayMean: 19.5,
			maxTemperature5dayMean: 24.5,
			totalRainDuration5dayMean: 1.8,
			averagePressure5dayMean: 1012.0,
			averageGlobalRadiation5dayMean: 215.0,
			cloudiness5dayMean: 0.25,
			publicHolidayAargau: 0,
			publicHolidayZug: 0,
			publicHolidaySchwyz: 0,
			publicHolidayStGallen: 0,
			publicHolidayThurgau: 0,
			publicHolidaySchaffhausen: 0,
			publicHolidayZurich: 0
		}
	});
	predictionMap.set('2024-08-28', {
		prediction: 15,
		featuresUsed: {
			averageTemperature: 20.0,
			maxTemperature: 25.0,
			totalRainDuration: 2.0,
			averagePressure: 1010.0,
			averageGlobalRadiation: 220.0,
			cloudiness: 0.3,
			moonPhase: 40.0,
			isVacationAargau: 0,
			isVacationZug: 0,
			isVacationSchwyz: 0,
			isVacationStGallen: 0,
			isVacationSchaffhausen: 0,
			isVacationThurgau: 0,
			weekday: 5,
			isWeekend: 1,
			aargauWeekAfterHoliday: 0,
			aargauFirstWeekOfHoliday: 0,
			zugWeekAfterHoliday: 0,
			zugFirstWeekOfHoliday: 0,
			schwyzWeekAfterHoliday: 0,
			schwyzFirstWeekOfHoliday: 0,
			stGallenWeekAfterHoliday: 0,
			stGallenFirstWeekOfHoliday: 0,
			schaffhausenWeekAfterHoliday: 0,
			schaffhausenFirstWeekOfHoliday: 0,
			thurgauWeekAfterHoliday: 0,
			thurgauFirstWeekOfHoliday: 0,
			averageTemperature5dayMean: 19.5,
			maxTemperature5dayMean: 24.5,
			totalRainDuration5dayMean: 1.8,
			averagePressure5dayMean: 1012.0,
			averageGlobalRadiation5dayMean: 215.0,
			cloudiness5dayMean: 0.25,
			publicHolidayAargau: 0,
			publicHolidayZug: 0,
			publicHolidaySchwyz: 0,
			publicHolidayStGallen: 0,
			publicHolidayThurgau: 0,
			publicHolidaySchaffhausen: 0,
			publicHolidayZurich: 0
		}
	});
	predictionMap.set('2024-08-29', {
		prediction: 17,
		featuresUsed: {
			averageTemperature: 20.0,
			maxTemperature: 25.0,
			totalRainDuration: 2.0,
			averagePressure: 1010.0,
			averageGlobalRadiation: 220.0,
			cloudiness: 0.3,
			moonPhase: 40.0,
			isVacationAargau: 0,
			isVacationZug: 0,
			isVacationSchwyz: 0,
			isVacationStGallen: 0,
			isVacationSchaffhausen: 0,
			isVacationThurgau: 0,
			weekday: 5,
			isWeekend: 1,
			aargauWeekAfterHoliday: 0,
			aargauFirstWeekOfHoliday: 0,
			zugWeekAfterHoliday: 0,
			zugFirstWeekOfHoliday: 0,
			schwyzWeekAfterHoliday: 0,
			schwyzFirstWeekOfHoliday: 0,
			stGallenWeekAfterHoliday: 0,
			stGallenFirstWeekOfHoliday: 0,
			schaffhausenWeekAfterHoliday: 0,
			schaffhausenFirstWeekOfHoliday: 0,
			thurgauWeekAfterHoliday: 0,
			thurgauFirstWeekOfHoliday: 0,
			averageTemperature5dayMean: 19.5,
			maxTemperature5dayMean: 24.5,
			totalRainDuration5dayMean: 1.8,
			averagePressure5dayMean: 1012.0,
			averageGlobalRadiation5dayMean: 215.0,
			cloudiness5dayMean: 0.25,
			publicHolidayAargau: 0,
			publicHolidayZug: 0,
			publicHolidaySchwyz: 0,
			publicHolidayStGallen: 0,
			publicHolidayThurgau: 0,
			publicHolidaySchaffhausen: 0,
			publicHolidayZurich: 0
		}
	});
	predictionMap.set('2024-08-30', {
		prediction: 12,
		featuresUsed: {
			averageTemperature: 20.0,
			maxTemperature: 25.0,
			totalRainDuration: 2.0,
			averagePressure: 1010.0,
			averageGlobalRadiation: 220.0,
			cloudiness: 0.3,
			moonPhase: 40.0,
			isVacationAargau: 0,
			isVacationZug: 0,
			isVacationSchwyz: 0,
			isVacationStGallen: 0,
			isVacationSchaffhausen: 0,
			isVacationThurgau: 0,
			weekday: 5,
			isWeekend: 1,
			aargauWeekAfterHoliday: 0,
			aargauFirstWeekOfHoliday: 0,
			zugWeekAfterHoliday: 0,
			zugFirstWeekOfHoliday: 0,
			schwyzWeekAfterHoliday: 0,
			schwyzFirstWeekOfHoliday: 0,
			stGallenWeekAfterHoliday: 0,
			stGallenFirstWeekOfHoliday: 0,
			schaffhausenWeekAfterHoliday: 0,
			schaffhausenFirstWeekOfHoliday: 0,
			thurgauWeekAfterHoliday: 0,
			thurgauFirstWeekOfHoliday: 0,
			averageTemperature5dayMean: 19.5,
			maxTemperature5dayMean: 24.5,
			totalRainDuration5dayMean: 1.8,
			averagePressure5dayMean: 1012.0,
			averageGlobalRadiation5dayMean: 215.0,
			cloudiness5dayMean: 0.25,
			publicHolidayAargau: 0,
			publicHolidayZug: 0,
			publicHolidaySchwyz: 0,
			publicHolidayStGallen: 0,
			publicHolidayThurgau: 0,
			publicHolidaySchaffhausen: 0,
			publicHolidayZurich: 0
		}
	});
	predictionMap.set('2024-08-31', {
		prediction: 3,
		featuresUsed: {
			averageTemperature: 20.0,
			maxTemperature: 25.0,
			totalRainDuration: 2.0,
			averagePressure: 1010.0,
			averageGlobalRadiation: 220.0,
			cloudiness: 0.3,
			moonPhase: 40.0,
			isVacationAargau: 0,
			isVacationZug: 0,
			isVacationSchwyz: 0,
			isVacationStGallen: 0,
			isVacationSchaffhausen: 0,
			isVacationThurgau: 0,
			weekday: 5,
			isWeekend: 1,
			aargauWeekAfterHoliday: 0,
			aargauFirstWeekOfHoliday: 0,
			zugWeekAfterHoliday: 0,
			zugFirstWeekOfHoliday: 0,
			schwyzWeekAfterHoliday: 0,
			schwyzFirstWeekOfHoliday: 0,
			stGallenWeekAfterHoliday: 0,
			stGallenFirstWeekOfHoliday: 0,
			schaffhausenWeekAfterHoliday: 0,
			schaffhausenFirstWeekOfHoliday: 0,
			thurgauWeekAfterHoliday: 0,
			thurgauFirstWeekOfHoliday: 0,
			averageTemperature5dayMean: 19.5,
			maxTemperature5dayMean: 24.5,
			totalRainDuration5dayMean: 1.8,
			averagePressure5dayMean: 1012.0,
			averageGlobalRadiation5dayMean: 215.0,
			cloudiness5dayMean: 0.25,
			publicHolidayAargau: 0,
			publicHolidayZug: 0,
			publicHolidaySchwyz: 0,
			publicHolidayStGallen: 0,
			publicHolidayThurgau: 0,
			publicHolidaySchaffhausen: 0,
			publicHolidayZurich: 0
		}
	});
	predictionMap.set('2024-09-01', {
		prediction: 1,
		featuresUsed: {
			averageTemperature: 20.0,
			maxTemperature: 25.0,
			totalRainDuration: 2.0,
			averagePressure: 1010.0,
			averageGlobalRadiation: 220.0,
			cloudiness: 0.3,
			moonPhase: 40.0,
			isVacationAargau: 0,
			isVacationZug: 0,
			isVacationSchwyz: 0,
			isVacationStGallen: 0,
			isVacationSchaffhausen: 0,
			isVacationThurgau: 0,
			weekday: 5,
			isWeekend: 1,
			aargauWeekAfterHoliday: 0,
			aargauFirstWeekOfHoliday: 0,
			zugWeekAfterHoliday: 0,
			zugFirstWeekOfHoliday: 0,
			schwyzWeekAfterHoliday: 0,
			schwyzFirstWeekOfHoliday: 0,
			stGallenWeekAfterHoliday: 0,
			stGallenFirstWeekOfHoliday: 0,
			schaffhausenWeekAfterHoliday: 0,
			schaffhausenFirstWeekOfHoliday: 0,
			thurgauWeekAfterHoliday: 0,
			thurgauFirstWeekOfHoliday: 0,
			averageTemperature5dayMean: 19.5,
			maxTemperature5dayMean: 24.5,
			totalRainDuration5dayMean: 1.8,
			averagePressure5dayMean: 1012.0,
			averageGlobalRadiation5dayMean: 215.0,
			cloudiness5dayMean: 0.25,
			publicHolidayAargau: 0,
			publicHolidayZug: 0,
			publicHolidaySchwyz: 0,
			publicHolidayStGallen: 0,
			publicHolidayThurgau: 0,
			publicHolidaySchaffhausen: 0,
			publicHolidayZurich: 0
		}
	});

	function roundedPrediction(date: string): number {
		console.log(date);
		console.log(predictionMap);
		let prediction = predictionMap.get(date);
		console.log(prediction);
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
</script>

<div class="h-full mx-auto">
	<div class="hero min-h-[50vh]">
		<div class="flex">
			<div class="">
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
