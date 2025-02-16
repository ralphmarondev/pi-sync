package com.ralphmarondev.pisync.ui.theme

import androidx.compose.material3.Typography
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import com.ralphmarondev.pisync.R

// Define different font families for different weights
val robotoMonoRegular = FontFamily(
    Font(R.font.roboto_mono_regular)
)

val robotoMonoBold = FontFamily(
    Font(R.font.roboto_mono_bold)
)

val robotoMonoThin = FontFamily(
    Font(R.font.roboto_mono_thin)
)

// Default Material 3 typography values
val baseline = Typography()

val Typography = Typography(
    displayLarge = baseline.displayLarge.copy(fontFamily = robotoMonoBold),
    displayMedium = baseline.displayMedium.copy(fontFamily = robotoMonoBold),
    displaySmall = baseline.displaySmall.copy(fontFamily = robotoMonoBold),
    headlineLarge = baseline.headlineLarge.copy(fontFamily = robotoMonoBold),
    headlineMedium = baseline.headlineMedium.copy(fontFamily = robotoMonoBold),
    headlineSmall = baseline.headlineSmall.copy(fontFamily = robotoMonoBold),
    titleLarge = baseline.titleLarge.copy(fontFamily = robotoMonoRegular),
    titleMedium = baseline.titleMedium.copy(fontFamily = robotoMonoRegular),
    titleSmall = baseline.titleSmall.copy(fontFamily = robotoMonoRegular),
    bodyLarge = baseline.bodyLarge.copy(fontFamily = robotoMonoRegular),
    bodyMedium = baseline.bodyMedium.copy(fontFamily = robotoMonoRegular),
    bodySmall = baseline.bodySmall.copy(fontFamily = robotoMonoRegular),
    labelLarge = baseline.labelLarge.copy(fontFamily = robotoMonoRegular),
    labelMedium = baseline.labelMedium.copy(fontFamily = robotoMonoRegular),
    labelSmall = baseline.labelSmall.copy(fontFamily = robotoMonoRegular),
)
