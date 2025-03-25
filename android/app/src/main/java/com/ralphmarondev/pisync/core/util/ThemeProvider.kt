package com.ralphmarondev.pisync.core.util

import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.compositionLocalOf

val LocalThemeState = compositionLocalOf<ThemeState> { error("ThemeState not provided") }

@Composable
fun ThemeProvider(
    themeState: ThemeState,
    content: @Composable () -> Unit
) {
    CompositionLocalProvider(LocalThemeState provides themeState) {
        content()
    }
}