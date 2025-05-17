package com.ralphmarondev.pisync.features.onboarding.presentation.components

import androidx.compose.material3.AlertDialog
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.text.font.FontFamily

@Composable
fun CompletedDialog(
    onDismiss: () -> Unit
) {
    AlertDialog(
        onDismissRequest = onDismiss,
        title = {
            Text(
                text = "Completed",
                fontFamily = FontFamily.Monospace
            )
        },
        text = {
            Text(
                text = "Onboarding completed. You can now proceed to login.",
                fontFamily = FontFamily.Monospace
            )
        },
        confirmButton = {
            TextButton(
                onClick = onDismiss
            ) {
                Text(
                    text = "Proceed",
                    fontFamily = FontFamily.Monospace
                )
            }
        },
        titleContentColor = MaterialTheme.colorScheme.primary,
        textContentColor = MaterialTheme.colorScheme.secondary
    )
}