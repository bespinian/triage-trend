export interface FeaturesUsed {
	averageTemperature: number;
	maxTemperature: number;
	totalRainDuration: number;
	averagePressure: number;
	averageGlobalRadiation: number;
	cloudiness: number;
	moonPhase: number;
	isVacationAargau: number;
	isVacationZug: number;
	isVacationSchwyz: number;
	isVacationStGallen: number;
	isVacationSchaffhausen: number;
	isVacationThurgau: number;
	weekday: number;
	isWeekend: number;
	aargauWeekAfterHoliday: number;
	aargauFirstWeekOfHoliday: number;
	zugWeekAfterHoliday: number;
	zugFirstWeekOfHoliday: number;
	schwyzWeekAfterHoliday: number;
	schwyzFirstWeekOfHoliday: number;
	stGallenWeekAfterHoliday: number;
	stGallenFirstWeekOfHoliday: number;
	schaffhausenWeekAfterHoliday: number;
	schaffhausenFirstWeekOfHoliday: number;
	thurgauWeekAfterHoliday: number;
	thurgauFirstWeekOfHoliday: number;
	averageTemperature5dayMean: number;
	maxTemperature5dayMean: number;
	totalRainDuration5dayMean: number;
	averagePressure5dayMean: number;
	averageGlobalRadiation5dayMean: number;
	cloudiness5dayMean: number;
	publicHolidayAargau: number;
	publicHolidayZug: number;
	publicHolidaySchwyz: number;
	publicHolidayStGallen: number;
	publicHolidayThurgau: number;
	publicHolidaySchaffhausen: number;
	publicHolidayZurich: number;
}

export interface Prediction {
	prediction: number;
	featuresUsed: FeaturesUsed;
}
