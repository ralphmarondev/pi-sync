package com.ralphmarondev.pisync.features.auth.presentation.components

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Info
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.sp

@Composable
fun ForgotPasswordDialog(
    onDismiss: () -> Unit,
    passwordHint: String
) {
    val hint = passwordHint.ifBlank {
        "No hint available."
    }

    AlertDialog(
        onDismissRequest = onDismiss,
        title = {
            Text(
                text = "Forgot Password?",
                color = MaterialTheme.colorScheme.primary
            )
        },
        text = {
            Text(
                text = hint,
                color = MaterialTheme.colorScheme.secondary,
                textAlign = TextAlign.Center,
                fontSize = 18.sp
            )
        },
        icon = {
            Icon(
                imageVector = Icons.Outlined.Info,
                contentDescription = null,
                tint = MaterialTheme.colorScheme.primary
            )
        },
        confirmButton = {
            TextButton(onClick = onDismiss) {
                Text(
                    text = "Close",
                    color = MaterialTheme.colorScheme.tertiary,
                    fontWeight = FontWeight.W500,
                    fontSize = 18.sp
                )
            }
        }
    )
}