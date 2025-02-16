package com.ralphmarondev.pisync.features.auth.presentation.components

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Password
import androidx.compose.material.icons.outlined.Visibility
import androidx.compose.material.icons.outlined.VisibilityOff
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.text.input.VisualTransformation
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.sp

@Composable
fun PasswordTextField(
    modifier: Modifier = Modifier,
    value: String,
    onValueChanged: (String) -> Unit,
    label: String,
    onDone: () -> Unit,
    leadingIcon: ImageVector = Icons.Outlined.Password
) {
    var show by remember { mutableStateOf(false) }

    OutlinedTextField(
        value = value,
        onValueChange = { onValueChanged(it) },
        modifier = modifier,
        label = {
            Text(
                text = label,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
        },
        textStyle = TextStyle(
            fontWeight = FontWeight.W500,
            fontSize = 16.sp,
            color = MaterialTheme.colorScheme.secondary
        ),
        singleLine = true,
        leadingIcon = {
            Icon(
                imageVector = leadingIcon,
                contentDescription = "",
                tint = MaterialTheme.colorScheme.secondary
            )
        },
        trailingIcon = {
            AnimatedVisibility(value.isNotEmpty()) {
                IconButton(onClick = { show = !show }) {
                    val icon = if (show) Icons.Outlined.Visibility else Icons.Outlined.VisibilityOff

                    Icon(
                        imageVector = icon,
                        contentDescription = "",
                        tint = MaterialTheme.colorScheme.secondary
                    )
                }
            }
        },
        visualTransformation = if (show) VisualTransformation.None else PasswordVisualTransformation(),
        keyboardOptions = KeyboardOptions(
            keyboardType = KeyboardType.Password,
            imeAction = ImeAction.Done
        ),
        keyboardActions = KeyboardActions(
            onDone = { onDone() }
        )
    )
}